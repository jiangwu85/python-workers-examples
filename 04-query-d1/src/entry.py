from workers import WorkerEntrypoint, Response


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        import asgi
        query = """
        SELECT quote, author
        FROM qtable
        ORDER BY RANDOM()
        LIMIT 1;
        """
        results = self.env.DB.prepare(query).all()
        data = results.results[0]
        # Return a JSON response
        print( Response.json(data))
        return await asgi.fetch(app, request.js_object, self.env)
