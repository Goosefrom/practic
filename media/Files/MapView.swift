//
//  MapView.swift
//  Landmarks
//
//  Created by Vlad Shelin on 03.01.2021.
//

import SwiftUI
import MapKit
struct MapView: View {
    @State private var region = MKCoordinateRegion(
            center: CLLocationCoordinate2D(latitude: 48.160_242, longitude: 24.499_990),
            span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
        )
    @State private var mapType: MKMapType = .satellite
    
    var body: some View {
        Map(coordinateRegion: $region)
    }
}

struct MapView_Previews: PreviewProvider {
    static var previews: some View {
        
        MapView()
    }
}
