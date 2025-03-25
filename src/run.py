from workflows.first_workflow import simple

def main() -> None:
    res = await simple.run({})


if __name__ == "__main__":
    main()
