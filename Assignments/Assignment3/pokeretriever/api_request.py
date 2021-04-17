import aiohttp
import asyncio


class APIHandlers:

	@staticmethod
	async def get_pokemon_data(id_: int, url: str, session: aiohttp.ClientSession):
		"""
		Get response from pokemon api.
		:param id_: parameter of the request
		:param url: a string
		:param session: an ClientSession Object.
		:return: a dictionary
		"""
		try:
			target_url = url.format(id_)
			response = await session.request(method="GET", url=target_url)
			json_dict = await response.json()
			return json_dict
		except aiohttp.ContentTypeError:
			return None

	@staticmethod
	async def process_single_request(id_: int, url: str):
		"""
		Get single response from an endpoint api.
		:param id_: parameter of the request
		:param url: a string
		:return: a dictionary
		"""
		async with aiohttp.ClientSession() as session:
			response = await APIHandlers.get_pokemon_data(id_, url, session)
			return response

	@staticmethod
	async def process_requests(requests: list, url: str):
		"""
		Get a list of responses from an endpoint.
		:param requests: a list of id_
		:param url: a string
		:return: a list of dictionary
		"""
		async with aiohttp.ClientSession() as session:
			pokemon_data = [APIHandlers.get_pokemon_data(id_, url, session) for id_ in requests]
			responses = await asyncio.gather(*pokemon_data)
			return responses
