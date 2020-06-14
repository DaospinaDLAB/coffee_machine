spin_particle = input()
electric_charge_particle = input()

if spin_particle == '1/2' and electric_charge_particle == '-1/3':
    print("Strange Quark")
elif spin_particle == '1/2' and electric_charge_particle == '2/3':
    print("Charm Quark")
elif spin_particle == '1/2' and electric_charge_particle == '-1':
    print("Electron Lepton")
elif spin_particle == '1/2' and electric_charge_particle == '0':
    print("Muon Lepton")
elif spin_particle == '1' and electric_charge_particle == '0':
    print("Photon Boson")
elif spin_particle == '0' and electric_charge_particle == '0':
    print("Higgs boson Boson")