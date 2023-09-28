from json import dump


async def export_data(directory: str, filename: int, content: dict) -> None:
    with open(f"{directory}{filename}.json", "w") as data:
        dump(content, data, indent=2, ensure_ascii=False)
