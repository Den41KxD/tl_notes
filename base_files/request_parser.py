from datetime import datetime
from typing import TypedDict, Optional

from django.utils.dateparse import parse_datetime

from user.models import User


class QueryParams(TypedDict):
	start_datetime: Optional[datetime]
	end_datetime: Optional[datetime]
	user: User


class RequestParser:
	
	def __init__(self, request):
		self.request = request
		
	
	def parse(self) -> QueryParams:
		
		return QueryParams(
			start_datetime=parse_datetime(self.request.GET.get('start_datetime')),
			end_datetime=parse_datetime(self.request.GET.get('end_datetime')),
			user=self.request.user
		)