from database import Database
from motoristaDAO import MotoristaDAO
from CLI import MotoristaCLI

db = Database(database="ex_avaliativo_1_BD2", collection="Motoristas")
motoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()