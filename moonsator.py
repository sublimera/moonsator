"""
moonsator: advanced code transformation and obfuscation library
developed by hexakleo hexakleo - 2025
transforms python code into an encrypted bytecode representation
"""

import base64,zlib,marshal,datetime,getpass
from typing import Dict, Any

class moonsator:
    """core transformation engine"""
    
    def __init__(self):
        """initialize with current timestamp and user"""
    
    def _create_loader(self, encoded_data: bytes) -> str:
        """create executable loader with clear output"""
        byte_list = list(encoded_data)
        
        return f"""
import marshal as m,zlib as z
_=bytes({byte_list})
def __():
 try:
  return m.loads(z.decompress(_))
 except:
  print("error: failed to decode")
  return None
exec(__(),globals())
"""

    def transform(self, source_code: str, output_file: str) -> Dict[str, Any]:
        """transform and protect the source code"""
        try:
            code_obj = compile(source_code, '<hexcore>', 'exec')
            protected = zlib.compress(marshal.dumps(code_obj), level=9)
            loader = self._create_loader(protected)
        
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(loader)
            
            return {
                "status": "success",
                "file": output_file,
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
