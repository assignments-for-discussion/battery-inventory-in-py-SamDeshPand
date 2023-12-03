
def count_batteries_by_health(present_capacities):
  ratedCapacity=120
  counts={ "healthy": 0, "exchange": 0, "failed": 0}
  for capacity in present_capacities:
    stateOfHealth=float(100*(capacity)/ratedCapacity)
    if stateOfHealth>80:
      counts["healthy"]=counts["healthy"]+1
    elif stateOfHealth<=80 and stateOfHealth>62:
      counts["exchange"]=counts["exchange"]+1
    else :
      counts["failed"]=counts["failed"]+1
  return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  
  empty_input=[]  #Test case to check empty input
  counts = count_batteries_by_health(empty_input)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  
  min_soh=[0] #Test case to check minimum input
  counts = count_batteries_by_health(min_soh)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 1)
  
  max_soh=[120] #Test case to check maximum input
  counts = count_batteries_by_health(max_soh)
  assert(counts["healthy"] == 1)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  
  soh_equals80=[96] #Test case to check maximum input for battery to be in exchange state
  counts = count_batteries_by_health(soh_equals80)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 1)
  assert(counts["failed"] == 0)
  
  print("All Test Cases Passed :)")
  

if __name__ == '__main__':
  test_bucketing_by_health()
