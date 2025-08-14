from database.DB_connect import DBConnect
from model.airports import Airport


class Dao:

    @staticmethod
    def getAllAirports():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * from airports a"""
            cursor.execute(query)
            for row in cursor:
                result.append(Airport(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllConnections():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select f.ORIGIN_AIRPORT_ID as origin_airport_id, f.DESTINATION_AIRPORT_ID as destination_airport_id, avg(f.DISTANCE) as distance, count(*) as count
                        from flights f 
                        group by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID """
            cursor.execute(query)
            for row in cursor:
                result.append(row)
            cursor.close()
            cnx.close()
        return result
