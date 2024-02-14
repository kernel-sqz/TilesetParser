from TilesetParser.src.find_tile import find_matching_tile
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Find a tile in the tileset library")
    parser.add_argument(
        "source_image_path", help="Path to single source tile you need to find", type=str)
    parser.add_argument(
        "tiles_folder", help="Path to tileset folder you want to parse", type=str)
    parser.add_argument("-s",
                        "--size", help='Size of a tile (default: 32)', type=int, default=32)
    parser.add_argument("-q",
                        "--similarity", help='Similarity level for openCV (default: 0.8)', type=float, default=0.8)
    parser.add_argument("-e",
                        "--extension", help='Extension of the files (default: bmp)', type=str, default='bmp')
    args = parser.parse_args()

    target_dir = Path(args.source_image_path)
    source_dir = Path(args.source_image_path)

    if not target_dir or not source_dir:
        return print("Error: Selected path does not exist!")

    return find_matching_tile(args.source_image_path, args.tiles_folder,
                              args.size, args.similarity, args.extension)


if __name__ == '__main__':
    main()
