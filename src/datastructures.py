"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""
#Family structure sirve para manejar los datos de los miembros de la familia
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # Este método genera un ID único para cada miembro nuevo
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    # Agrega un nuevo miembro a la lista de miembros de la familia
    def add_member(self, member):
        member['last_name'] = self.last_name
        if member.get('id') is None:
            member['id'] = self._generate_id()
        else:
            if member['id'] >= self._next_id:
                self._next_id = member['id'] + 1
        self._members.append(member)
        return member
    # Elimina un miembro de la lista de miembros de la familia por su ID
    def delete_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                self._members.remove(member)
                return True
        return False
    # Devuelve un miembro de la lista de miembros de la familia por su ID
    def get_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                return member
        return None

    # Este método devuelve una lista con todos los miembros de la familia   
    def get_all_members(self):
        return self._members
