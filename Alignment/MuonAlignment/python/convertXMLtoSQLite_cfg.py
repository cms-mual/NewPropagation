import FWCore.ParameterSet.Config as cms

process = cms.Process("CONVERT")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

# process.load("Configuration.StandardSequences.GeometryDB_cff")
# process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Configuration.StandardSequences.GeometryIdeal_cff")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.MuonGeometryDBConverter = cms.EDAnalyzer("MuonGeometryDBConverter",
    input = cms.string("xml"),
    fileName = cms.string("REPLACEME.xml"),
    shiftErr = cms.double(1000.),
    angleErr = cms.double(6.28),
    output = cms.string("db"))

process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBSetup,
    connect = cms.string("sqlite_file:REPLACEME.db"),
    toPut = cms.VPSet(
        cms.PSet(record = cms.string("DTAlignmentRcd"), tag = cms.string("DTAlignmentRcd")),
        cms.PSet(record = cms.string("DTAlignmentErrorRcd"), tag = cms.string("DTAlignmentErrorRcd")),
        cms.PSet(record = cms.string("CSCAlignmentRcd"), tag = cms.string("CSCAlignmentRcd")),
        cms.PSet(record = cms.string("CSCAlignmentErrorRcd"), tag = cms.string("CSCAlignmentErrorRcd"))))

process.inertGlobalPositionRcd = cms.ESSource("PoolDBESSource",
    process.CondDBSetup,
    connect = cms.string("sqlite_file:inertGlobalPositionRcd.db"),
    toGet = cms.VPSet(cms.PSet(record = cms.string("GlobalPositionRcd"), tag = cms.string("inertGlobalPositionRcd"))))

process.Path = cms.Path(process.MuonGeometryDBConverter)
