from datetime import datetime
from airline.models import Reservation


class ReservationRepository:
    """
    Clase de repositorio que se encargará de conectarse con la base de datos
    para manipular reservas.
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
        """
        Crea una nueva reserva.

        Args:
            status: Estado de la reserva.
            reservation_date: Fecha de la reserva.
            price: Precio total de la reserva.
            reservation_code: Código único de reserva.
            flight_id: ID del vuelo asociado.
            passenger_id: ID del pasajero asociado.
            seat_id: ID del asiento reservado.

        Returns:
            Instancia de la reserva creada.
        """
        return Reservation.objects.create(
            status=status,
            reservation_date=reservation_date,
            price=price,
            reservation_code=reservation_code,
            flight_id=flight_id,
            passenger_id=passenger_id,
            seat_id=seat_id,
        )

    @staticmethod
    def delete(reservation: Reservation) -> bool:
        """
        Elimina una reserva de la base de datos.

        Args:
            reservation: Instancia de la reserva a eliminar.

        Returns:
            True si la eliminación fue exitosa.

        Raises:
            ValueError: Si la reserva no existe.
        """
        try:
            reservation.delete()
        except Reservation.DoesNotExist:
            raise ValueError("La reserva no existe")

    @staticmethod
    def update(
        Reservation: Reservation,
        status: str,
        reservation_date: datetime,
        price: float,
        reservation_code: str,
        flight_id: int,
        passenger_id: int,
        seat_id: int
    ) -> Reservation:
        """
        Actualiza los datos de una reserva.

        Args:
            Reservation: Instancia de la reserva a actualizar.
            status: Nuevo estado.
            reservation_date: Nueva fecha de reserva.
            price: Nuevo precio.
            reservation_code: Nuevo código de reserva.
            flight_id: Nuevo ID de vuelo.
            passenger_id: Nuevo ID de pasajero.
            seat_id: Nuevo ID de asiento.

        Returns:
            Instancia actualizada de la reserva.
        """
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
        Obtiene todas las reservas registradas.

        Returns:
            Lista de reservas.
        """
        return Reservation.objects.all()

    @staticmethod
    def get_by_id(reservation_id: int) -> Reservation:
        """
        Obtiene una reserva por su ID.

        Args:
            Reservation_id: ID de la reserva.

        Returns:
            Instancia de la reserva o None si no existe.
        """
        try:
            return Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return None

    @staticmethod
    def search_by_reservation_code(reservation_code: str) -> list[Reservation]:
        """
        Busca reservas cuyo código contenga el texto dado.

        Args:
            reservation_code: Texto parcial o completo del código.

        Returns:
            Lista de reservas coincidentes.
        """
        return Reservation.objects.filter(reservation_code__icontains=reservation_code)
