from django.db.models import Q, Count
from rest_framework import generics

from listings.models import BookingInfo, Blocked
from .serializers import BookingInfoSerializer

class BookingInfoViewSet(generics.ListAPIView):
    serializer_class = BookingInfoSerializer
    def get_queryset(self):
        max_price = self.request.query_params.get('max_price')
        check_in  = self.request.query_params.get('check_in')
        check_out = self.request.query_params.get('check_out')
        queryset = BookingInfo.objects.all()
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if check_in and check_out:
            blocked_listing = Blocked.objects.filter(Q(check_in__lte=check_in, check_out__lte=check_in) | Q(check_in__gte=check_out, check_out__gte=check_out))

            blocked_listing_dict = {} #generating the dict key=title, value=counter in previous ORM query
            fullRooms = {}            #generating the dict that we want to delete from our list
            for item in blocked_listing:
                title = item.get_title()
                total_room_count = item.get_total_room_count()

                if title not in fullRooms:
                    if title not in blocked_listing_dict.keys():
                        blocked_listing_dict[title] = 0
                    blocked_listing_dict[title] += 1

                    if blocked_listing_dict[title] >= total_room_count: #if the current counter is equal or bigger than the available rooms
                        fullRooms[title] = item.id
                        blocked_listing_dict.pop(title)

            queryset = queryset.exclude(blocked_info__id__in=fullRooms.values())
        return queryset.order_by('price')
