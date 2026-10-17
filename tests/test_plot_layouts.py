import tempfile
import unittest
from pathlib import Path
from ring_star.experiment_plots import plot_campaign


class PlotLayoutTests(unittest.TestCase):
    def test_more_than_eight_instances_are_not_truncated(self):
        rows=[{"instance":f"case_{i}","n":10+i,"p":3,"alpha":1.,"method":"greedy",
               "mean_cost":10.,"std_cost":None,"mean_seconds":.01,"std_seconds":None,"statuses":"{}"}
              for i in range(9)]
        with tempfile.TemporaryDirectory() as tmp:
            paths=plot_campaign(rows,Path(tmp))
            self.assertEqual(len(paths),9)
            self.assertTrue((Path(tmp)/"by_instance/case_8_alpha_1.png").exists())


if __name__=="__main__":unittest.main()
