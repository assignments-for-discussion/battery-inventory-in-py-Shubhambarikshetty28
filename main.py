def count_batteries_by_health(present_capacities):
  rated_capacity=120
  count=count1=count2=0
  for i in present_capacities:
         Soh=(100*present_capacities(i))/rated_capacity
         if Soh>=80 and Soh<=100:
               count=count+1
         if Soh<80 and Soh>=62:
               count1=count1+1
         if Soh<62:
               count2=count2+1
  return {
        "healthy": count,
        "exchange": count1,
        "failed": count2
  }


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
