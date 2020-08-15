import matlab.engine
eng = matlab.engine.start_matlab()
KnowStateSequence = matlab.double([1, 1, 2, 1, 3, 3, 4, 1, 3, 4, 1, 1, 2, 1, 5, 5, 5, 5, 1, 1, \
                    3, 3, 1, 4, 4, 3, 3, 1, 4, 1, 1, 1, 1, 2, 1])
eng.workspace['KnowStateSequence'] = KnowStateSequence
eng.eval('cd ~/git/oneshot/Codes/KFF_LFM_HMM/Test', nargout=0)
# eng.eval('''KnowStateSequence = [1, 1, 2, 1, 3, 3, 4, 1, 3, 4, 1, 1, 2, 1, 5, 5, 5, 5, 1, 1, ...
#                      3, 3, 1, 4, 4, 3, 3, 1, 4, 1, 1, 1, 1, 2, 1]''', nargout=0)
PeriodOfEachState = matlab.double([30])
eng.workspace['PeriodOfEachState'] = PeriodOfEachState
# eng.eval('PeriodOfEachState = 30', nargout=0)
model = eng.eval('''gphmm_test_argparse('experimentNo', 1000, 'ModelName', 'KFFLFMHMM', ...
'dataSetName', 'BlendMotion', ...
'OptimisationMethod', 'MultiStart', ...
'PretrainOptimiser', 'MultiStart', ...
'ParamsInitMethod', 'GuessParams', ...
'WeightFlag', 'Default', ...
'GDIters', 10, 'PretrainParams', 0, ...
'PretrainMethod', 'Supervised', ...
'em_max_iter', 50, 'EmissionProbForHMMFlag', 'log', ...
'NormaliseEmissionProbFlag', 1, 'PeriodOfEachState', PeriodOfEachState, ...
'nlf', 2, 'NumberOfStates', 5, ...
'PretrainIters', 400, 'GDStartIter', 3, ...
'SpecifyObjectiveGradient', true, 'OperationOnWeightedValue', 'ModelOrngSegLog', ...
'PretrainMaxAllowedTry', 10, ...
'PretrainStopThreshold', -4000, 'PretrainParallelFlag', 0, ...
'ParallelFlag', 1, 'em_max_iterPost', 1, 'GDItersPost', 100, ...
'NumberOfFrequences', 20, ...
'FixedGamma', sparse(KnowStateSequence, 1: length(KnowStateSequence), 1, 5, length(KnowStateSequence)), ...
'DataPointsLength', length(KnowStateSequence) * PeriodOfEachState * 2, ...
'MainFrequencyFindMethod', 'SecondPeakAmplitude')''', nargout=1)
#model, parser = matlab.engine.gphmm_test_BlendMotion(nargout=2)
# eng.eval('PeriodOfEachState = 30', nargout=0)
# model = eng.eval('''sparse(KnowStateSequence, 1: length(KnowStateSequence), 1, 5, length(KnowStateSequence))''', nargout=1)