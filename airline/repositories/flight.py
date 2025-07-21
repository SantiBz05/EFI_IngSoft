from airline.models import Flight, Plane, User

from datetime import datetime, timedelta

class FlightRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manupilar vuelos
    """

    @staticmethod
    def create(
        origin: str,
        destination: str,
        departure_date: datetime,
        arrival_date: datetime,
        duration: timedelta,
        status: str,
        base_price: float,
        plane_id: int,
        user_id: list[int],
    ) -> Flight:
        plane = Plane.objects.get(id=plane_id)

        flight = Flight.objects.create(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            arrival_date=arrival_date,
            duration= duration,
            status= status,
            base_price= base_price,
            plane_id = plane,
        )
        users = User.objects.filter(id__in=user_id)
        flight.user_id.set(users)
        return flight

    
    @staticmethod
    def delete(flight: Flight) -> bool:
        try:
            flight.delete()
        except Flight.DoesNotExist:
            raise ValueError("El Vuelo No Existe")
        
    @staticmethod
    def update(flight: Flight, origin: str, destination: str, departure_date: str, arrival_date: str, duration: str, status: str, base_price: float, plane_id: int, user_id: int) -> Flight:
        flight.origin = origin
        flight.destination = destination
        flight.departure_date = departure_date
        flight.arrival_date = arrival_date
        flight.duration = duration
        flight.status = status
        flight.base_price = base_price
        flight.plane_id = plane_id
        flight.user_id = user_id
        flight.save()

        return flight
    
    @staticmethod 
    def get_all() -> list[Flight]:
        """
        Obtiene todos los objetos (vuelos)
        """
        return Flight.objects.all()
    
    @staticmethod
    def get_by_id(flight_id: int) -> Flight:
        """
        Obtiene un vuelo a partir de su id
        """
        try:
            return Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return None

    @staticmethod
    def search_by_origin(origin: str) -> list[Flight]:
        """
        Buscar el vuelo que contenga el origen ingresado
        """
        return  Flight.objects.filter(origin__icontains=origin)
    
    