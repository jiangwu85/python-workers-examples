from workers import WorkerEntrypoint, Response


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        query = """
        SELECT quote, author
        FROM qtable
        ORDER BY RANDOM()
        LIMIT 1;
        """
        results = await self.env.DB.prepare(query).all()
        data = results.results[0]

        env = request.scope["env"]
        msg = await env.MESSAGE

        # Return a JSON response
        return Response.json({"data": data,"env":msg})
