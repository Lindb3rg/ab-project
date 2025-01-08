
from . import models
from datetime import datetime, timedelta







def create_db_objects(n_objects):
    for i in range(1, (n_objects+1)):
        models.Song.objects.create(
            name=f"Song {i}",
            starting_date=datetime.now(),
            duration=timedelta(minutes=i),
            status="WRITING",
            notes=f"This is the notes for song number {i}"
        )
    print("20 songs have been created!")






    


