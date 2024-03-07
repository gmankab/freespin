# license is gnu agpl 3 - gnu.org/licenses/agpl-3.0.en.html

from pathlib import Path
import asyncio
import sys


if __name__ == '__main__':
    sys.path.append(
        str(Path(__file__).parent.resolve())
    )
    from .core import main
    asyncio.run(main.main())

