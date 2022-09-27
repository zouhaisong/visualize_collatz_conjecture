

from functools import cache
from functools import wraps
def log_and_call(statement):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{statement} inputs: {args}")            
            ret = func(*args, **kwargs)
            print(f"{statement} outputs: {ret}")
            return ret 
        return wrapper
    return decorator

@cache
def collatz_route(num:int)->list:
  ret = []
  while(num!=1):
    ret.append(num)
    num = collatz_rule(num)
  ret.append(1)  
  return ret

# @cache
# @log_and_call("collatz_rule:")
def collatz_rule(num:int):
  if num <= 1:
    raise Exception("collatz_rule num should large or equal than 1 !")
    
  if num % 2 == 0:
    return int(num / 2)
  else:
    return num * 3 + 1

# @log_and_call("collatz_dict:")
def collatz_dict(num:int)->dict:
  ret = {}
  cur_num = num
  while(cur_num>1 and cur_num not in ret):
    next_num = collatz_rule(cur_num)
    ret[cur_num]=next_num
    cur_num=next_num
  return ret

# @log_and_call("collatz_dict_le:")
def collatz_dict_le(max:int)->dict:
  ret = {}
  for i in range(2,max+1):
    cur_num = i
    while(cur_num>1 and cur_num not in ret):
      next_num = collatz_rule(cur_num)
      ret[cur_num]=next_num
      cur_num=next_num
      
  return ret

def main():
  collatz_rule(2)

if __name__=="__main__":
  main()
  print("== DONE ==")