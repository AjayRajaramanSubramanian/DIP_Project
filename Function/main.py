import dippykit as dip 
import matlab.engine
eng = matlab.engine.start_matlab()



class Evaluation_Metrics:
    def __init__(self):
        pass  

    def psnr(self, img1, img2):
        return dip.metrics.PSNR(img1, img2)

    def mse(self, img1, img2):
        return dip.metrics.MSE(img1, img2)

    def ssim(self, img1, img2):
        return dip.metrics.SSIM(img1, img2)

    def unique(self, img1, img2):
        return eng.mslUNIQUE(img1, img2)

    def ms_unique(self, img1, img2):
        return eng.mslMSUNIQUE(img1, img2)

    def summer(self, img1, img2):
        return eng.SUMMER(img1, img2)

    def csv(self, img1, img2):
        return eng.csv(img1, img2)
