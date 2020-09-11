#!/usr/bin/python
# -*- coding: utf-8 -*-
import aiohttp
import asyncio
from aiohttp.typedefs import URL
from colorama import Fore, Style, init
from typing import Any, NoReturn, Union

init()

TIMEOUT: int = 5
URL_A: str = "https://example.com"
URL_C: str = "https://nexup.com"


def _print_job_status(job_name: str, status: str, colour: Any) -> NoReturn:
    print(
        Style.BRIGHT + Fore.WHITE + job_name + colour + " " + status + Style.RESET_ALL
    )


def print_job_started(job_name: str) -> NoReturn:
    _print_job_status(job_name=job_name, status="STARTED", colour=Fore.LIGHTYELLOW_EX)


def print_job_finished(job_name: str) -> NoReturn:
    _print_job_status(job_name=job_name, status="FINISHED", colour=Fore.BLUE)


async def request(
        session: aiohttp.ClientSession,
        method: str,
        url: Union[str, URL],
        timeout: int = TIMEOUT,
        **kwargs
) -> aiohttp.ClientResponse:
    async with session.request(method=method, url=url, timeout=timeout, **kwargs) as response:
        return response


async def fun_a(session: aiohttp.ClientSession) -> aiohttp.ClientResponse:
    print_job_started("fun_a")
    response = await request(session=session, method="get", url=URL_A)
    print_job_finished("fun_a")
    return response


async def fun_b(session: aiohttp.ClientSession) -> aiohttp:
    print_job_started("fun_b")
    response_a = await fun_a(session=session)
    response_b = await request(session=session, method="get", url=response_a.url)
    print_job_finished("fun_b")
    return response_b


async def fun_c(session: aiohttp.ClientSession) -> aiohttp.ClientResponse:
    print_job_started("fun_c")
    response_c = await request(session=session, method="get", url=URL_C)
    print_job_finished("fun_c")
    return response_c


async def _main():
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*[
            asyncio.ensure_future(fun_b(session=session)),
            asyncio.ensure_future(fun_b(session=session)),
            asyncio.ensure_future(fun_b(session=session)),
            asyncio.ensure_future(fun_c(session=session)),
            asyncio.ensure_future(fun_c(session=session)),
            asyncio.ensure_future(fun_c(session=session)),
        ])


def main():
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(_main())
    return loop.run_until_complete(future)


if __name__ == '__main__':
    res = main()
    for r in res:
        print(r.url)
