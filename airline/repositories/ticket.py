from airline.models import Ticket

class TicketRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manupilar boletos

    """

    @staticmethod
    def create(
        barcode: str,
        issue_date: str,
        status: str,
        reservation_id: str,
    ) -> Ticket:
        return Ticket.objects.create(
            barcode=barcode,
            issue_date=issue_date,
            status=status,
            reservation_id=reservation_id,
        )
    
    @staticmethod
    def delete(ticket: Ticket) -> bool:
        try:
            ticket.delete()
        except Ticket.DoesNotExist:
            raise ValueError("El Boleto No Existe")
        
    @staticmethod
    def update(ticket: Ticket, barcode: str, issue_date: str, status: str, reservation_id: str) -> Ticket:
        ticket.barcode = barcode
        ticket.issue_date = issue_date
        ticket.status = status
        ticket.reservation_id = reservation_id
        ticket.save()

        return Ticket
    
    @staticmethod 
    def get_all() -> list[Ticket]:
        """
        Obtiene todos los objetos (boletos)
        """
        return Ticket.objects.all()
    
    @staticmethod
    def get_by_id(plane_id: int) -> Ticket:
        """
        Obtiene un boleto a partir de su id
        """
        try:
            return Ticket.objects.get(id=plane_id)
        except Ticket.DoesNotExist:
            return None

    @staticmethod
    def search_by_barcode(barcode: str) -> list[Ticket]:
        """
        Buscar el boleto que contenga el codigo de barra ingresado
        """
        return  Ticket.objects.filter(barcode__icontains=barcode)
    
    