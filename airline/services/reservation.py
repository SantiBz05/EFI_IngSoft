from airline.models import Reservation
from airline.repositories.reservation import ReservationRepository

class ReservationService:

    @staticmethod
    def create(
        status: str,
        reservation_date: int,
        price: int,
        reservation_code: int,
        flight_id: int,
        passenger_id: int,
        seat_id: int,
    ) -> Reservation:
        return ReservationRepository.create(
            status=status,
            reservation_date=reservation_date,
            price=price,
            reservation_code=reservation_code,
            flight_id=flight_id,
            passenger_id=passenger_id,
            seat_id=seat_id,
        )

    @staticmethod
    def delete(reservation_id: int) -> bool:
        reservation = ReservationRepository.get_by_id(reservation_id=reservation_id)
        if reservation:
            return ReservationRepository.delete(Reservation=Reservation)
        return False
    
    @staticmethod
    def update(
        reservation_id: int,
        status: str,
        reservation_date: int,
        price: int,
        reservation_code: int,
        flight_id: int,
        passenger_id: int,
        seat_id: int,
    ) -> bool:
        reservation = ReservationRepository.get_by_id(reservation_id=reservation_id)
        if reservation:
            ReservationRepository.update(
                reservation=reservation,
                status=status,
                reservation_date=reservation_date,
                price=price,
                reservation_code=reservation_code,
                flight_id=flight_id,
                passenger_id=passenger_id,
                seat_id=seat_id,
            )

    @staticmethod
    def get_all() -> list[Reservation]:
        return ReservationRepository.get_all() 
    
    @staticmethod
    def get_by_id(reservation_id: int) -> list[Reservation]:
        if reservation_id:
            return ReservationRepository.get_by_id(reservation_id=reservation_id)
        return ValueError("El Avion No Existe")
    
    @staticmethod
    def search_by_status(status: str) -> list[Reservation]:
        if status:
            return ReservationRepository.search_by_status(status=status)
        return ValueError("El Avion No Existe")