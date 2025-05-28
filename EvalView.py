from db.mysql_connector import get_connection

class EvalView:
    def getEval(self, select_date) -> list:

        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
                SELECT content, rating
                FROM eval
                WHERE write_date = %s
            """
            cursor.execute(query, (select_date,))
            rows = cursor.fetchall()

            review_list = []
            for content, rating in rows:
                review = {
                    "content": content,
                    "rating": rating
                }
                review_list.append(review)

            return review_list

        except Exception as e:
            print(f"리뷰 조회 중 오류 발생: {e}")
            return []

        finally:
            conn.close()