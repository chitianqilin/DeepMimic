import gphmm
AGPHMM = gphmm.initialize()
# model, parser = AGPHMM.gphmm_test_argparse('dataSetName', 'BlendMotion', nargout=2)
model, parser = AGPHMM.gphmm_test_argparse(nargout=2)
