function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const trimmedCookie = cookie.trim();
            if (trimmedCookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(trimmedCookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("DOMContentLoaded", () => {

    const popup = document.getElementById("note-popup");
    let popupTextEditor = null;  // Editor instance will be stored here
    const closePopup = document.querySelector(".close-popup");
    const savePopup = document.querySelector(".save-popup");
    let currentNoteId = null;

    document.querySelectorAll('.note-text').forEach((element) => {
        element.addEventListener('click', () => {
            const fullText = element.getAttribute('data-full-text');
            const noteId = element.getAttribute('data-field-id')
            // Уничтожить предыдущий экземпляр редактора если существует
            if (popupTextEditor) {
                popupTextEditor.destroy().then(() => {
                    initializeEditor(fullText, noteId);
                }).catch(error => {
                    console.error('Error destroying CKEditor:', error);
                });
            } else {
                initializeEditor(fullText, noteId);
            }

            currentNoteId = element.getAttribute('data-note-id');
            popup.style.display = "block";
        });
    });

    closePopup.addEventListener('click', () => {
        closePopupFunction();
    });

    window.addEventListener('click', (event) => {
        if (event.target === popup) {
            closePopupFunction();
        }
    });

    // Обработчик для сохранения текста
    savePopup.addEventListener('click', () => {
        if (!popupTextEditor) return;
        const updatedText = popupTextEditor.getData();

        const currentNoteId = popupTextEditor.noteId;
        if (currentNoteId) {
            fetch(`/notes/note/${currentNoteId}/`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({text: updatedText})
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    if (data.status === 'success') {
                        // Обновите текст на странице или выполните другие действия
                        popup.style.display = "none";
                        const noteElement = document.querySelector(`[data-note-id="${currentNoteId}"]`);
                        if (noteElement) {
                            noteElement.setAttribute('data-full-text', updatedText);
                            noteElement.innerHTML = updatedText;
                        }
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        }
    });

    // Функция закрытия попапа и разрушения экземпляра редактора CKEditor
    function closePopupFunction() {
        popup.style.display = "none";
        console.log('Popup closed');
        if (popupTextEditor) {
            popupTextEditor.destroy().catch(error => {
                console.error('Error destroying CKEditor:', error);
            });
            popupTextEditor = null;
        }
        currentNoteId = null;
    }

    // Функция для инициализации редактора CKEditor
    function initializeEditor(content, noteId) {
        ClassicEditor
            .create(document.querySelector('#popup-text'))
            .then(editor => {
                popupTextEditor = editor;
                popupTextEditor.setData(content);
                popupTextEditor.noteId = noteId;
            })
            .catch(error => {
                console.error('Error initializing CKEditor:', error);
            });
    }


});

function filterRecords() {
    const startDatetime = document.getElementById('start_datetime').value;
    const endDatetime = document.getElementById('end_datetime').value;
    const params = new URLSearchParams();

    if (startDatetime) {
        params.append('start_datetime', startDatetime);
    }
    if (endDatetime) {
        params.append('end_datetime', endDatetime);
    }

    window.location.href = `${window.location.pathname}?${params.toString()}`;
}

function generateReport(button) {
    button.disabled = true
    const startDatetime = document.getElementById('start_datetime').value;
    const endDatetime = document.getElementById('end_datetime').value;
    const currentLanguage = document.documentElement.lang; // Извлечение языка
    console.log(currentLanguage);
    fetch(`/${currentLanguage}/notes/start_generate_report/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(
            {
                start_datetime: startDatetime,
                end_datetime: endDatetime
            })
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Обновите текст на странице или выполните другие действия
                console.log(data)
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}