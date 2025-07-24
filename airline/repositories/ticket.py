from datetime import datetime
from airline.models import Ticket


class TicketRepository:
    """
    Clase de repositorio que se encargará de conectarse con la base de datos
    para manipular boletos.
    """

    @staticmethod
    def create(
        barcode: str,
        issue_date: datetime,
        status: str,
        reservation: str,
    ) -> Ticket:
        """
        Crea un nuevo boleto.

        Args:
            barcode: Código de barras del boleto.
            issue_date: Fecha de emisión.
            status: Estado actual del boleto.
            reservation: ID de la reserva asociada.

        Returns:
            Instancia del boleto creado.
        """
        return Ticket.objects.create(
            barcode=barcode,
            issue_date=issue_date,
            status=status,
            reservation=reservation,
        )

    @staticmethod
    def delete(ticket: Ticket) -> bool:
        """
        Elimina un boleto.

        Args:
            ticket: Instancia del boleto a eliminar.

        Returns:
            True si se elimina correctamente.

        Raises:
            ValueError: Si el boleto no existe.
        """
        try:
            ticket.delete()
            return True
        except Ticket.DoesNotExist:
            raise ValueError("El boleto no existe")

    @staticmethod
    def update(
        ticket: Ticket,
        barcode: str,
        issue_date: datetime,
        status: str,
        reservation: str
    ) -> Ticket:
        """
        Actualiza los datos de un boleto.

        Args:
            ticket: Instancia del boleto a actualizar.
            barcode: Nuevo código de barras.
            issue_date: Nueva fecha de emisión.
            status: Nuevo estado.
            reservation: Nueva reserva asociada.

        Returns:
            Instancia del boleto actualizada.
        """
        ticket.barcode = barcode
        ticket.issue_date = issue_date
        ticket.status = status
        ticket.reservation = reservation
        ticket.save()

        return Ticket

    @staticmethod
    def get_all() -> list[Ticket]:
        """
        Obtiene todos los boletos registrados.

        Returns:
            Lista de boletos.
        """
        return Ticket.objects.all()

    @staticmethod
    def get_by_id(plane_id: int) -> Ticket:
        """
        Obtiene un boleto por su ID.

        Args:
            plane_id: ID del boleto.

        Returns:
            Instancia del boleto o None si no existe.
        """
        try:
            return Ticket.objects.get(id=plane_id)
        except Ticket.DoesNotExist:
            return None

    @staticmethod
    def search_by_barcode(barcode: str) -> list[Ticket]:
        """
        Busca boletos cuyo código de barras contenga el texto ingresado.

        Args:
            barcode: Texto parcial del código.

        Returns:
            Lista de boletos coincidentes.
        """
        return Ticket.objects.filter(barcode__icontains=barcode)
