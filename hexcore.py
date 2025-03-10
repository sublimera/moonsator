"""
hexcore: advanced code transformation and obfuscation library
developed by hexakleo (alterkleo) - 2025
transforms python code into an encrypted bytecode representation
"""

import base64
import zlib
import marshal
import datetime
import getpass
from typing import Dict, Any

class hexcore:
    """core transformation engine"""
    
    def __init__(self):
        """initialize with current timestamp and user"""
        self.timestamp = "2025-03-10 07:56:36"
        self.author = "alterkleo"
        self.version = "2.5.0"
    
    def _create_loader(self, encoded_data: bytes) -> str:
        """create executable loader with clear output"""
        byte_list = list(encoded_data)
        
        return f'''#!/usr/bin/env python
# timestamp: {self.timestamp}
# author: {self.author}
# engine: hexcore v{self.version}

import marshal as m,zlib as z
_=bytes({byte_list})
def __():
 try:
  return m.loads(z.decompress(_))
 except:
  print("error: failed to decode")
  return None
exec(__(),globals())
'''

    def transform(self, source_code: str, output_file: str) -> Dict[str, Any]:
        """transform and protect the source code"""
        try:
            # compile to bytecode
            code_obj = compile(source_code, '<hexcore>', 'exec')
            
            # marshal and compress
            protected = zlib.compress(marshal.dumps(code_obj), level=9)
            
            # generate loader
            loader = self._create_loader(protected)
            
            # save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(loader)
            
            return {
                "status": "success",
                "file": output_file,
                "info": {
                    "time": self.timestamp,
                    "author": self.author,
                    "version": self.version
                }
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }