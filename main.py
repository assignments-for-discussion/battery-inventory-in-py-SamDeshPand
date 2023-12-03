
def count_batteries_by_health(present_capacities):
  dict={ "healthy": 0, "exchange": 0, "failed": 0}
  for battery in present_capacities:
    SoH=float(100*(battery)/120)
    if SoH>80:
      dict["healthy"]=dict["healthy"]+1
    elif SoH<=80 and SoH>62:
      dict["exchange"]=dict["exchange"]+1
    else :
      dict["failed"]=dict["failed"]+1
  return dict


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
