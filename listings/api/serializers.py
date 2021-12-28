from rest_framework import serializers
from listings.models import BookingInfo

class BookingInfoSerializer(serializers.ModelSerializer):

    listing_type = serializers.SerializerMethodField('get_listing_type')
    title = serializers.SerializerMethodField('get_title')
    country = serializers.SerializerMethodField('get_country')
    city = serializers.SerializerMethodField('get_city')

    class Meta:
        model = BookingInfo
        fields = ['listing_type', 'title', 'country', 'city', 'price', ]

    def get_listing_type(self, bookingInfo):
        if bookingInfo.listing:
            return "Apartment"
        else:
            return "Hotel"

    def get_title(self, bookingInfo):
        if bookingInfo.listing:
            return bookingInfo.listing.title
        else:
            return bookingInfo.hotel_room_type.hotel.title

    def get_country(self, bookingInfo):
        if bookingInfo.listing:
            return bookingInfo.listing.country
        else:
            return bookingInfo.hotel_room_type.hotel.country

    def get_city(self, bookingInfo):
        if bookingInfo.listing:
            return bookingInfo.listing.city
        else:
            return bookingInfo.hotel_room_type.hotel.city

