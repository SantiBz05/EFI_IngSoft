from airline.models import Plane

class PlaneRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manupilar aviones
    """

    @staticmethod
    def create(
        model: str,
        capacity: int,
        rows: int,
        columns: int,
    ) -> Plane:
        return Plane.objects.create(
            model=model,
            capacity=capacity,
            rows=rows,
            columns=columns,
        )
    
    @staticmethod
    def delete(plane: Plane) -> bool:
        try:
            plane.delete()
        except Plane.DoesNotExist:
            raise ValueError("El Avion No Existe")
        
    @staticmethod
    def update(plane: Plane, model: str, capacity: int, rows: int, columns: int) -> Plane:
        plane.model = model
        plane.capacity = capacity
        plane.rows = rows
        plane.columns = columns
        plane.save()

        return plane
    
    @staticmethod 
    def get_all() -> list[Plane]:
        """
        Obtiene todos los objetos (Aviones)
        """
        return Plane.objects.all()
    
    @staticmethod
    def get_by_id(plane_id: int) -> Plane:
        """
        Obtiene un avion a partir de su id
        """
        try:
            return Plane.objects.get(id=plane_id)
        except Plane.DoesNotExist:
            return None

    @staticmethod
    def search_by_model(model: str) -> list[Plane]:
        """
        Buscar el avion que contenga el model ingresado
        """
        try:
            return Plane.objects.filter(model__icontains=model)
        except Plane.DoesNotExist:
            return None
