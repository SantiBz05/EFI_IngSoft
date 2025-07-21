from airline.models import Reservation
from datetime import datetime

class ReservationRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manupilar reservas
    """

    @staticmethod
    def create(
        status: str,
        reservation_date: datetime,
        price: float,
        reservation_code: str,
        flight_id: int,
        passenger_id: int,
        seat_id: int,

    ) -> Reservation:
        return Reservation.objects.create(
            status=status,
            reservation_date=reservation_date,
            price=price,
            reservation_code=reservation_code,
            flight_id= flight_id,
            passenger_id= passenger_id,
            seat_id= seat_id,
        )
    
    @staticmethod
    def delete(reservation: Reservation) -> bool:
        try:
            reservation.delete()
        except Reservation.DoesNotExist:
            raise ValueError("El reserva No Existe")
        
    @staticmethod
    def update(Reservation: Reservation, status: str, reservation_date: datetime, price: float, reservation_code: str, flight_id: int, passenger_id: int, seat_id: int) -> Reservation:
        Reservation.status = status
        Reservation.reservation_date = reservation_date
        Reservation.price = price
        Reservation.reservation_code = reservation_code
        Reservation.flight_id = flight_id
        Reservation.passenger_id = passenger_id
        Reservation.seat_id = seat_id
        Reservation.save()

        return Reservation
    
    @staticmethod 
    def get_all() -> list[Reservation]:
        """
        Obtiene todos los objetos (reservas)
        """
        return Reservation.objects.all()
    
    @staticmethod
    def get_by_id(Reservation_id: int) -> Reservation:
        """
        Obtiene un reserva a partir de su id
        """
        try:
            return Reservation.objects.get(id=Reservation_id)
        except Reservation.DoesNotExist:
            return None

    @staticmethod
    def search_by_reservation_code(reservation_code: str) -> list[Reservation]:
        """
        Buscar el reserva que contenga el codigo de reserva ingresado
        """
        return  Reservation.objects.filter(reservation_code__icontains=reservation_code)
    
    