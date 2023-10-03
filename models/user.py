class User:
  def __init__(self, id, name, email, password, timestamp):
    self.id = id
    self.email = email
    self.name = name
    self.password = password
    self.timestamp = timestamp

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'email': self.email,
      'name': self.name,
      'password': self.password,
      'timestamp':self.timestamp
    }