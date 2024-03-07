import core.args
import asyncio


async def main():
    args = core.args.parse_args()
    match args.mode:
        case 'autotests':
            import autotests.main
            await autotests.main.main()
        case 'bot':
            print('test')


if __name__ == '__main__':
    asyncio.run(main())

