import imp

from datetime import date

def test_allocating_to_a_batch_reduces_the_available_quantaity():
    batch = Batch("batch-001","SMALL_TABLE",qty=20,eta = date.today())
    line = OrderLine("order-ref","SMALL-TABLE",2)

    batch.allocate(line)

    assert batch.available_quantity ==18