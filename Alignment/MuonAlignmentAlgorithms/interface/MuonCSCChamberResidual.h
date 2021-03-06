#ifndef Alignment_MuonAlignmentAlgorithms_MuonCSCChamberResidual_H
#define Alignment_MuonAlignmentAlgorithms_MuonCSCChamberResidual_H

/** \class MuonCSCChamberResidual
 * 
 * Implementation of muon chamber residuals for CSC
 * 
 * $Id: $
 */

#include "Alignment/MuonAlignmentAlgorithms/interface/MuonHitsChamberResidual.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"

class MuonCSCChamberResidual: public MuonHitsChamberResidual
{
public:
  MuonCSCChamberResidual(edm::ESHandle<GlobalTrackingGeometry> globalGeometry, AlignableNavigator *navigator,
                         DetId chamberId, AlignableDetOrUnitPtr chamberAlignable);

  // for CSC, the residual is chamber local x, projected by the strip measurement direction
  // for CSC, the resslope is dresx/dz, or tan(phi_y)
  /* virtual void addResidual(const TrajectoryStateOnSurface *tsos, const TransientTrackingRecHit *hit); */
  virtual void addResidual(edm::ESHandle<Propagator> prop, const TrajectoryStateOnSurface *tsos, const TrackingRecHit *hit);

  // dummy method
  virtual void setSegmentResidual(const reco::MuonChamberMatch *, const reco::MuonSegmentMatch *) {}
};

#endif // Alignment_MuonAlignmentAlgorithms_MuonCSCChamberResidual_H
