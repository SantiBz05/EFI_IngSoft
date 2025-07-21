from airline.models import Ticket
from airline.repositories.ticket import TicketRepository

from datetime import datetime

class TicketService:

    @staticmethod
    def create(
        barcode: str,
        issue_date: datetime,
        status: str,
        reservation_id: int,
    ) -> Ticket:
        return TicketRepository.create(
            barcode=barcode,
            issue_date=issue_date,
            status=status,
            reservation_id=reservation_id,
        )

    @staticmethod
    def delete(ticket_id: int) -> bool:
        ticket = TicketRepository.get_by_id(ticket_id=ticket_id)
        if ticket:
            return TicketRepository.delete(ticket=ticket)
        return False
    
    @staticmethod
    def update(
        ticket_id: int,
        barcode: str,
        issue_date: int,
        status: str,
        reservation_id: int,
    ) -> bool:
        ticket = TicketRepository.get_by_id(ticket_id=ticket_id)
        if Ticket:
            TicketRepository.update(
                ticket=ticket,
                barcode=barcode,
                issue_date=issue_date,
                status=status,
                reservation_id=reservation_id,
            )

    @staticmethod
    def get_all() -> list[Ticket]:
        return TicketRepository.get_all() 
    
    @staticmethod
    def get_by_id(ticket_id: int) -> list[Ticket]:
        if ticket_id:
            return TicketRepository.get_by_id(ticket_id=ticket_id)
        return ValueError("El Ticket No Existe")
    
    @staticmethod
    def search_by_barcode(barcode: str) -> list[Ticket]:
        if barcode:
            return TicketRepository.search_by_barcode(barcode=barcode)
        return ValueError("El Ticket No Existe")