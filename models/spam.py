class Spam:
  def __init__(self, id, message, timestamp):
    self.id = id
    self.message = message
    self.timestamp = timestamp

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'message': self.message,
      'timestamp':self.timestamp
    }