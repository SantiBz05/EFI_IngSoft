from airline.models import Seat

class SeatRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manupilar asientos
    """

    @staticmethod
    def create(
        number: str,
        row: int,
        column: str,
        seat_type: str,
        status: str,
        plane_id: int,
    ) -> Seat:
        return Seat.objects.create(
            number=number,
            row=row,
            column=column,
            seat_type=seat_type,
            status= status,
            plane_id= plane_id,
        )
    
    @staticmethod
    def delete(seat: Seat) -> bool:
        try:
            seat.delete()
        except Seat.DoesNotExist:
            raise ValueError("El asientos No Existe")
        
    @staticmethod
    def update(seat: Seat, number: str, row: int, column: str, seat_type: str, status: str, plane_id: int) -> Seat:
        seat.number = number
        seat.row = row
        seat.column = column
        seat.seat_type = seat_type
        seat.status = status
        seat.plane_id = plane_id
        seat.save()

        return Seat
    
    @staticmethod 
    def get_all() -> list[Seat]:
        """
        Obtiene todos los objetos (asientoss)
        """
        return Seat.objects.all()
    
    @staticmethod
    def get_by_id(Seat_id: int) -> Seat:
        """
        Obtiene un asientos a partir de su id
        """
        try:
            return Seat.objects.get(id=Seat_id)
        except Seat.DoesNotExist:
            return None

    @staticmethod
    def search_by_number(number: str) -> list[Seat]:
        """
        Buscar el asientos que contenga el numero ingresado
        """
        return  Seat.objects.filter(number__icontains=number)
    
    