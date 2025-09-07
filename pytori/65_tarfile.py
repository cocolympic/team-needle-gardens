import tarfile
import os
from pathlib import Path

def create_tar_archive(source_dir, archive_name):
    with tarfile.open(archive_name, 'w:gz') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    print(f"アーカイブ '{archive_name}' を作成しました")
