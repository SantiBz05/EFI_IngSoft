from airline.models import Seat


class SeatRepository:
    """
    Clase de repositorio que se encargará de conectarse con la base de datos
    para manipular asientos.
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
        """
        Crea un nuevo asiento.

        Args:
            number: Número identificador del asiento.
            row: Fila en la que se encuentra.
            column: Columna en la que se encuentra.
            seat_type: Tipo de asiento (ej: ventana, pasillo).
            status: Estado actual del asiento.
            plane_id: ID del avión al que pertenece.

        Returns:
            Instancia del asiento creado.
        """
        return Seat.objects.create(
            number=number,
            row=row,
            column=column,
            seat_type=seat_type,
            status=status,
            plane_id=plane_id,
        )

    @staticmethod
    def delete(seat: Seat) -> bool:
        """
        Elimina un asiento.

        Args:
            seat: Instancia del asiento a eliminar.

        Returns:
            True si se elimina correctamente.

        Raises:
            ValueError: Si el asiento no existe.
        """
        try:
            seat.delete()
            return True
        except Seat.DoesNotExist:
            raise ValueError("El asiento no existe")

    @staticmethod
    def update(
        seat: Seat,
        number: str,
        row: int,
        column: str,
        seat_type: str,
        status: str,
        plane_id: int
    ) -> Seat:
        """
        Actualiza los datos de un asiento.

        Args:
            seat: Instancia del asiento a actualizar.
            number: Nuevo número del asiento.
            row: Nueva fila.
            column: Nueva columna.
            seat_type: Nuevo tipo.
            status: Nuevo estado.
            plane_id: Nuevo avión asociado.

        Returns:
            Instancia actualizada del asiento.
        """
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
        Obtiene todos los objetos (asientos).

        Returns:
            Lista de todos los asientos.
        """
        return Seat.objects.all()

    @staticmethod
    def get_by_id(Seat_id: int) -> Seat:
        """
        Obtiene un asiento por su ID.

        Args:
            Seat_id: ID del asiento.

        Returns:
            Instancia del asiento o None si no existe.
        """
        try:
            return Seat.objects.get(id=Seat_id)
        except Seat.DoesNotExist:
            return None

    @staticmethod
    def search_by_number(number: str) -> list[Seat]:
        """
        Busca asientos cuyo número contenga el texto ingresado.

        Args:
            number: Texto parcial del número.

        Returns:
            Lista de asientos coincidentes.
        """
        return Seat.objects.filter(number__icontains=number)
