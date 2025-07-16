from airline.models import Passenger

class PassengerRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manupilar pasajeros
    """

    @staticmethod
    def create(
        name: str,
        document: str,
        document_type: str,
        email: str,
        phone: str,
        birth_date: str,
    ) -> Passenger:
        return Passenger.objects.create(
            name=name,
            document=document,
            document_type=document_type,
            email=email,
            phone= phone,
            birth_date= birth_date,
        )
    
    @staticmethod
    def delete(passenger: Passenger) -> bool:
        try:
            passenger.delete()
        except Passenger.DoesNotExist:
            raise ValueError("El Pasajero No Existe")
        
    @staticmethod
    def update(passenger: Passenger, name: str, document: str, document_type: str, email: str, phone: str, birth_date: str) -> Passenger:
        passenger.name = name
        passenger.document = document
        passenger.document_type = document_type
        passenger.email = email
        passenger.phone = phone
        passenger.birth_date = birth_date
        passenger.save()

        return Passenger
    
    @staticmethod 
    def get_all() -> list[Passenger]:
        """
        Obtiene todos los objetos (pasajeros)
        """
        return Passenger.objects.all()
    
    @staticmethod
    def get_by_id(passenger_id: int) -> Passenger:
        """
        Obtiene un pasajero a partir de su id
        """
        try:
            return Passenger.objects.get(id=passenger_id)
        except Passenger.DoesNotExist:
            return None

    @staticmethod
    def search_by_name(name: str) -> list[Passenger]:
        """
        Buscar el pasajero que contenga el nombre ingresado
        """
        return  Passenger.objects.filter(name__icontains=name)
    
    