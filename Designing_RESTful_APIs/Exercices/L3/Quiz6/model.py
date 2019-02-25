from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    image_url = Column(String)

    @property
    def serialize(self):
        return dict(id = self.id,
                    name = self.name,
                    address = self.address,
                    image_url = self.image_url)

engine = create_engine('sqlite:///mashup.db?check_same_thread=False', echo=True)
Base.metadata.create_all(engine)
