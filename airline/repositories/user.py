from airline.models import User

class UserRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manupilar usuarios

    """

    @staticmethod
    def create(
        username: str,
        password: str,
        email: str,
        role: str,
    ) -> User:
        return User.objects.create(
            username=username,
            password=password,
            email=email,
            role=role,
        )
    
    @staticmethod
    def delete(user: User) -> bool:
        try:
            user.delete()
        except User.DoesNotExist:
            raise ValueError("El Usuario No Existe")
        
    @staticmethod
    def update(user: User, username: str, password: str, email: str, role: str) -> User:
        user.username = username
        user.password = password
        user.email = email
        user.role = role
        user.save()

        return user
    
    @staticmethod 
    def get_all() -> list[User]:
        """
        Obtiene todos los objetos (Usuarios)
        """
        return User.objects.all()
    
    @staticmethod
    def get_by_id(user_id: int) -> User:
        """
        Obtiene un usuario a partir de su id
        """
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def search_by_username(username: str) -> list[User]:
        """
        Buscar el usuario que contenga el nombre ingresado
        """
        return  User.objects.filter(username__icontains=username)
    
    