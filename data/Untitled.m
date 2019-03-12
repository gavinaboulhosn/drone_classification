clear;
samp_drop = 15000;
cap_tot = 9;
drone_ctrl = {'FRSKY0000','phantom_4PRO0000','T14SG0000'};
sig_pk_all = {};
sig_all = {};
for idx_dr = 1:length(drone_ctrl)
    for idx = 1:cap_tot
        load([drone_ctrl{idx_dr} num2str(idx) '.mat'])
        temp = double(Channel_1.Data);
%         temp = haart(temp,1);
%         temp1 = downsample(temp,100);
        temp1 = temp(2.49e6:2.51e6);
%         temp1 = temp(6.22e5:6.32e5);
%           temp1 = temp(2.95e5:3.27e5);

%         temp1 = temp1/std(temp1);
%         temp1 = temp(samp_drop+1:end);
% %         temp1_pk_idx = find(islocalmax(temp1,'MinProminence',1000,'MinSeparation',20));
%         temp1_pk_idx = find(islocalmax(temp1));
%         temp1_pk = temp1(temp1_pk_idx);
        sig_pk_all{idx_dr,idx} = temp1;
        sig_all{idx_dr,idx} = temp1;
    end
end