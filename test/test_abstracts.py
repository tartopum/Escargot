import escargot as es



def test_init_abstract():
    obj = es.AbstractRamp(accuracy=0.5, max_len=200)

def test_init_angle_valve():
    obj = es.angle_valve.AbstractRamp(
        len_args=(1, 1),
        short_args=(1, 1),
        max_angle=90,
        accuracy=0.5,
        max_len=200
    )
