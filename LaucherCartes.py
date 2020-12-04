from controllers import maincontroller
from utils import log

if __name__ == '__main__':
    log.Logger.Instance().appinfo('Launching Cartes CPx NG...')
    c = maincontroller.Controller()
    c.run()
