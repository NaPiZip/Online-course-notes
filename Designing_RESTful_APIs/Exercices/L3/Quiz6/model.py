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
                    restaurant_name = self.name,
                    restaurant_address = self.address,
                    restaurant_image = self.image_url)

engine = create_engine('sqlite:///mashup.db', echo=True)
Base.metadata.create_all(engine)
