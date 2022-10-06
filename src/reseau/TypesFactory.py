from src.reseau.types.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
from src.reseau.types.AccountTagInformation import AccountTagInformation
from src.reseau.types.PlayerSearchCharacterNameInformation import PlayerSearchCharacterNameInformation
from src.reseau.types.PlayerSearchTagInformation import PlayerSearchTagInformation
from src.reseau.types.StatisticData import StatisticData
from src.reseau.types.StatisticDataBoolean import StatisticDataBoolean
from src.reseau.types.StatisticDataByte import StatisticDataByte
from src.reseau.types.StatisticDataInt import StatisticDataInt
from src.reseau.types.StatisticDataShort import StatisticDataShort
from src.reseau.types.StatisticDataString import StatisticDataString
from src.reseau.types.GameServerInformations import GameServerInformations
from src.reseau.types.Achievement import Achievement
from src.reseau.types.AchievementAchieved import AchievementAchieved
from src.reseau.types.AchievementAchievedRewardable import AchievementAchievedRewardable
from src.reseau.types.AchievementObjective import AchievementObjective
from src.reseau.types.AchievementStartedObjective import AchievementStartedObjective
from src.reseau.types.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from src.reseau.types.AbstractFightDispellableEffect import AbstractFightDispellableEffect
from src.reseau.types.FightTemporaryBoostEffect import FightTemporaryBoostEffect
from src.reseau.types.FightTemporaryBoostStateEffect import FightTemporaryBoostStateEffect
from src.reseau.types.FightTemporaryBoostWeaponDamagesEffect import FightTemporaryBoostWeaponDamagesEffect
from src.reseau.types.FightTemporarySpellBoostEffect import FightTemporarySpellBoostEffect
from src.reseau.types.FightTemporarySpellImmunityEffect import FightTemporarySpellImmunityEffect
from src.reseau.types.FightTriggeredEffect import FightTriggeredEffect
from src.reseau.types.GameActionMark import GameActionMark
from src.reseau.types.GameActionMarkedCell import GameActionMarkedCell
from src.reseau.types.ServerSessionConstant import ServerSessionConstant
from src.reseau.types.ServerSessionConstantInteger import ServerSessionConstantInteger
from src.reseau.types.ServerSessionConstantLong import ServerSessionConstantLong
from src.reseau.types.ServerSessionConstantString import ServerSessionConstantString
from src.reseau.types.AbstractCharacterInformation import AbstractCharacterInformation
from src.reseau.types.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations
from src.reseau.types.CharacterMinimalAllianceInformations import CharacterMinimalAllianceInformations
from src.reseau.types.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
from src.reseau.types.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations
from src.reseau.types.CharacterMinimalInformations import CharacterMinimalInformations
from src.reseau.types.CharacterMinimalPlusLookAndGradeInformations import CharacterMinimalPlusLookAndGradeInformations
from src.reseau.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from src.reseau.types.ActorAlignmentInformations import ActorAlignmentInformations
from src.reseau.types.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
from src.reseau.types.AlterationInfo import AlterationInfo
from src.reseau.types.CharacterCharacteristic import CharacterCharacteristic
from src.reseau.types.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from src.reseau.types.CharacterCharacteristics import CharacterCharacteristics
from src.reseau.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
from src.reseau.types.CharacterCharacteristicValue import CharacterCharacteristicValue
from src.reseau.types.CharacterSpellModification import CharacterSpellModification
from src.reseau.types.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from src.reseau.types.CharacterBaseInformations import CharacterBaseInformations
from src.reseau.types.CharacterHardcoreOrEpicInformations import CharacterHardcoreOrEpicInformations
from src.reseau.types.CharacterRemodelingInformation import CharacterRemodelingInformation
from src.reseau.types.CharacterToRemodelInformations import CharacterToRemodelInformations
from src.reseau.types.RemodelingInformation import RemodelingInformation
from src.reseau.types.DebtInformation import DebtInformation
from src.reseau.types.KamaDebtInformation import KamaDebtInformation
from src.reseau.types.PlayerNote import PlayerNote
from src.reseau.types.ActorRestrictionsInformations import ActorRestrictionsInformations
from src.reseau.types.PlayerStatus import PlayerStatus
from src.reseau.types.PlayerStatusExtended import PlayerStatusExtended
from src.reseau.types.ActorOrientation import ActorOrientation
from src.reseau.types.EntityDispositionInformations import EntityDispositionInformations
from src.reseau.types.EntityMovementInformations import EntityMovementInformations
from src.reseau.types.FightEntityDispositionInformations import FightEntityDispositionInformations
from src.reseau.types.GameContextActorInformations import GameContextActorInformations
from src.reseau.types.GameContextActorPositionInformations import GameContextActorPositionInformations
from src.reseau.types.GameRolePlayTaxCollectorInformations import GameRolePlayTaxCollectorInformations
from src.reseau.types.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
from src.reseau.types.MapCoordinates import MapCoordinates
from src.reseau.types.MapCoordinatesAndId import MapCoordinatesAndId
from src.reseau.types.MapCoordinatesExtended import MapCoordinatesExtended
from src.reseau.types.TaxCollectorStaticExtendedInformations import TaxCollectorStaticExtendedInformations
from src.reseau.types.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from src.reseau.types.AbstractFightTeamInformations import AbstractFightTeamInformations
from src.reseau.types.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation
from src.reseau.types.FightAllianceTeamInformations import FightAllianceTeamInformations
from src.reseau.types.FightCommonInformations import FightCommonInformations
from src.reseau.types.FightExternalInformations import FightExternalInformations
from src.reseau.types.FightLoot import FightLoot
from src.reseau.types.FightLootObject import FightLootObject
from src.reseau.types.FightOptionsInformations import FightOptionsInformations
from src.reseau.types.FightResultAdditionalData import FightResultAdditionalData
from src.reseau.types.FightResultExperienceData import FightResultExperienceData
from src.reseau.types.FightResultFighterListEntry import FightResultFighterListEntry
from src.reseau.types.FightResultListEntry import FightResultListEntry
from src.reseau.types.FightResultMutantListEntry import FightResultMutantListEntry
from src.reseau.types.FightResultPlayerListEntry import FightResultPlayerListEntry
from src.reseau.types.FightResultPvpData import FightResultPvpData
from src.reseau.types.FightResultTaxCollectorListEntry import FightResultTaxCollectorListEntry
from src.reseau.types.FightStartingPositions import FightStartingPositions
from src.reseau.types.FightTeamInformations import FightTeamInformations
from src.reseau.types.FightTeamLightInformations import FightTeamLightInformations
from src.reseau.types.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
from src.reseau.types.FightTeamMemberEntityInformation import FightTeamMemberEntityInformation
from src.reseau.types.FightTeamMemberInformations import FightTeamMemberInformations
from src.reseau.types.FightTeamMemberMonsterInformations import FightTeamMemberMonsterInformations
from src.reseau.types.FightTeamMemberTaxCollectorInformations import FightTeamMemberTaxCollectorInformations
from src.reseau.types.FightTeamMemberWithAllianceCharacterInformations import FightTeamMemberWithAllianceCharacterInformations
from src.reseau.types.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from src.reseau.types.GameContextSummonsInformation import GameContextSummonsInformation
from src.reseau.types.GameFightAIInformations import GameFightAIInformations
from src.reseau.types.GameFightCharacterInformations import GameFightCharacterInformations
from src.reseau.types.GameFightCharacteristics import GameFightCharacteristics
from src.reseau.types.GameFightEffectTriggerCount import GameFightEffectTriggerCount
from src.reseau.types.GameFightEntityInformation import GameFightEntityInformation
from src.reseau.types.GameFightFighterEntityLightInformation import GameFightFighterEntityLightInformation
from src.reseau.types.GameFightFighterInformations import GameFightFighterInformations
from src.reseau.types.GameFightFighterLightInformations import GameFightFighterLightInformations
from src.reseau.types.GameFightFighterMonsterLightInformations import GameFightFighterMonsterLightInformations
from src.reseau.types.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from src.reseau.types.GameFightFighterNamedLightInformations import GameFightFighterNamedLightInformations
from src.reseau.types.GameFightFighterTaxCollectorLightInformations import GameFightFighterTaxCollectorLightInformations
from src.reseau.types.GameFightMonsterInformations import GameFightMonsterInformations
from src.reseau.types.GameFightMonsterWithAlignmentInformations import GameFightMonsterWithAlignmentInformations
from src.reseau.types.GameFightMutantInformations import GameFightMutantInformations
from src.reseau.types.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo
from src.reseau.types.GameFightSpellCooldown import GameFightSpellCooldown
from src.reseau.types.GameFightTaxCollectorInformations import GameFightTaxCollectorInformations
from src.reseau.types.SpawnCharacterInformation import SpawnCharacterInformation
from src.reseau.types.SpawnCompanionInformation import SpawnCompanionInformation
from src.reseau.types.SpawnInformation import SpawnInformation
from src.reseau.types.SpawnMonsterInformation import SpawnMonsterInformation
from src.reseau.types.SpawnScaledMonsterInformation import SpawnScaledMonsterInformation
from src.reseau.types.AllianceInformations import AllianceInformations
from src.reseau.types.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
from src.reseau.types.AnomalySubareaInformation import AnomalySubareaInformation
from src.reseau.types.AtlasPointsInformations import AtlasPointsInformations
from src.reseau.types.BasicAllianceInformations import BasicAllianceInformations
from src.reseau.types.BasicGuildInformations import BasicGuildInformations
from src.reseau.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from src.reseau.types.GameRolePlayActorInformations import GameRolePlayActorInformations
from src.reseau.types.GameRolePlayCharacterInformations import GameRolePlayCharacterInformations
from src.reseau.types.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from src.reseau.types.GameRolePlayGroupMonsterWaveInformations import GameRolePlayGroupMonsterWaveInformations
from src.reseau.types.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from src.reseau.types.GameRolePlayMerchantInformations import GameRolePlayMerchantInformations
from src.reseau.types.GameRolePlayMountInformations import GameRolePlayMountInformations
from src.reseau.types.GameRolePlayMutantInformations import GameRolePlayMutantInformations
from src.reseau.types.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from src.reseau.types.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from src.reseau.types.GameRolePlayNpcWithQuestInformations import GameRolePlayNpcWithQuestInformations
from src.reseau.types.GameRolePlayPortalInformations import GameRolePlayPortalInformations
from src.reseau.types.GameRolePlayPrismInformations import GameRolePlayPrismInformations
from src.reseau.types.GameRolePlayTreasureHintInformations import GameRolePlayTreasureHintInformations
from src.reseau.types.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from src.reseau.types.GroupMonsterStaticInformationsWithAlternatives import GroupMonsterStaticInformationsWithAlternatives
from src.reseau.types.GuildInAllianceInformations import GuildInAllianceInformations
from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.HumanInformations import HumanInformations
from src.reseau.types.HumanOption import HumanOption
from src.reseau.types.HumanOptionAlliance import HumanOptionAlliance
from src.reseau.types.HumanOptionEmote import HumanOptionEmote
from src.reseau.types.HumanOptionFollowers import HumanOptionFollowers
from src.reseau.types.HumanOptionGuild import HumanOptionGuild
from src.reseau.types.HumanOptionObjectUse import HumanOptionObjectUse
from src.reseau.types.HumanOptionOrnament import HumanOptionOrnament
from src.reseau.types.HumanOptionSkillUse import HumanOptionSkillUse
from src.reseau.types.HumanOptionSpeedMultiplier import HumanOptionSpeedMultiplier
from src.reseau.types.HumanOptionTitle import HumanOptionTitle
from src.reseau.types.MonsterBoosts import MonsterBoosts
from src.reseau.types.MonsterInGroupInformations import MonsterInGroupInformations
from src.reseau.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from src.reseau.types.ObjectItemInRolePlay import ObjectItemInRolePlay
from src.reseau.types.AlignmentWarEffortInformation import AlignmentWarEffortInformation
from src.reseau.types.BreachBranch import BreachBranch
from src.reseau.types.BreachReward import BreachReward
from src.reseau.types.ExtendedBreachBranch import ExtendedBreachBranch
from src.reseau.types.ExtendedLockedBreachBranch import ExtendedLockedBreachBranch
from src.reseau.types.ArenaLeagueRanking import ArenaLeagueRanking
from src.reseau.types.ArenaRankInfos import ArenaRankInfos
from src.reseau.types.ArenaRanking import ArenaRanking
from src.reseau.types.LeagueFriendInformations import LeagueFriendInformations
from src.reseau.types.DecraftedItemStackInfo import DecraftedItemStackInfo
from src.reseau.types.JobBookSubscription import JobBookSubscription
from src.reseau.types.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from src.reseau.types.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from src.reseau.types.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry
from src.reseau.types.JobCrafterDirectorySettings import JobCrafterDirectorySettings
from src.reseau.types.JobDescription import JobDescription
from src.reseau.types.JobExperience import JobExperience
from src.reseau.types.MapNpcQuestInfo import MapNpcQuestInfo
from src.reseau.types.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer
from src.reseau.types.NamedPartyTeam import NamedPartyTeam
from src.reseau.types.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
from src.reseau.types.PartyGuestInformations import PartyGuestInformations
from src.reseau.types.PartyInvitationMemberInformations import PartyInvitationMemberInformations
from src.reseau.types.PartyMemberArenaInformations import PartyMemberArenaInformations
from src.reseau.types.PartyMemberGeoPosition import PartyMemberGeoPosition
from src.reseau.types.PartyMemberInformations import PartyMemberInformations
from src.reseau.types.PartyEntityBaseInformation import PartyEntityBaseInformation
from src.reseau.types.PartyEntityMemberInformation import PartyEntityMemberInformation
from src.reseau.types.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
from src.reseau.types.QuestActiveDetailedInformations import QuestActiveDetailedInformations
from src.reseau.types.QuestActiveInformations import QuestActiveInformations
from src.reseau.types.QuestObjectiveInformations import QuestObjectiveInformations
from src.reseau.types.QuestObjectiveInformationsWithCompletion import QuestObjectiveInformationsWithCompletion
from src.reseau.types.PortalInformation import PortalInformation
from src.reseau.types.TreasureHuntFlag import TreasureHuntFlag
from src.reseau.types.TreasureHuntStep import TreasureHuntStep
from src.reseau.types.TreasureHuntStepDig import TreasureHuntStepDig
from src.reseau.types.TreasureHuntStepFight import TreasureHuntStepFight
from src.reseau.types.TreasureHuntStepFollowDirection import TreasureHuntStepFollowDirection
from src.reseau.types.TreasureHuntStepFollowDirectionToHint import TreasureHuntStepFollowDirectionToHint
from src.reseau.types.TreasureHuntStepFollowDirectionToPOI import TreasureHuntStepFollowDirectionToPOI
from src.reseau.types.BidExchangerObjectInfo import BidExchangerObjectInfo
from src.reseau.types.ForgettableSpellItem import ForgettableSpellItem
from src.reseau.types.GoldItem import GoldItem
from src.reseau.types.Item import Item
from src.reseau.types.ObjectEffects import ObjectEffects
from src.reseau.types.ObjectItem import ObjectItem
from src.reseau.types.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from src.reseau.types.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity
from src.reseau.types.ObjectItemMinimalInformation import ObjectItemMinimalInformation
from src.reseau.types.ObjectItemNotInContainer import ObjectItemNotInContainer
from src.reseau.types.ObjectItemQuantity import ObjectItemQuantity
from src.reseau.types.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from src.reseau.types.ObjectItemToSell import ObjectItemToSell
from src.reseau.types.ObjectItemToSellInBid import ObjectItemToSellInBid
from src.reseau.types.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop
from src.reseau.types.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop
from src.reseau.types.SellerBuyerDescriptor import SellerBuyerDescriptor
from src.reseau.types.SpellItem import SpellItem
from src.reseau.types.ObjectEffect import ObjectEffect
from src.reseau.types.ObjectEffectCreature import ObjectEffectCreature
from src.reseau.types.ObjectEffectDate import ObjectEffectDate
from src.reseau.types.ObjectEffectDice import ObjectEffectDice
from src.reseau.types.ObjectEffectDuration import ObjectEffectDuration
from src.reseau.types.ObjectEffectInteger import ObjectEffectInteger
from src.reseau.types.ObjectEffectLadder import ObjectEffectLadder
from src.reseau.types.ObjectEffectMinMax import ObjectEffectMinMax
from src.reseau.types.ObjectEffectMount import ObjectEffectMount
from src.reseau.types.ObjectEffectString import ObjectEffectString
from src.reseau.types.EntityInformation import EntityInformation
from src.reseau.types.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from src.reseau.types.FinishMoveInformations import FinishMoveInformations
from src.reseau.types.AbstractContactInformations import AbstractContactInformations
from src.reseau.types.AcquaintanceInformation import AcquaintanceInformation
from src.reseau.types.AcquaintanceOnlineInformation import AcquaintanceOnlineInformation
from src.reseau.types.FriendInformations import FriendInformations
from src.reseau.types.FriendOnlineInformations import FriendOnlineInformations
from src.reseau.types.FriendSpouseInformations import FriendSpouseInformations
from src.reseau.types.FriendSpouseOnlineInformations import FriendSpouseOnlineInformations
from src.reseau.types.IgnoredInformations import IgnoredInformations
from src.reseau.types.IgnoredOnlineInformations import IgnoredOnlineInformations
from src.reseau.types.Contribution import Contribution
from src.reseau.types.GuildEmblem import GuildEmblem
from src.reseau.types.GuildMember import GuildMember
from src.reseau.types.GuildRankInformation import GuildRankInformation
from src.reseau.types.GuildRankMinimalInformation import GuildRankMinimalInformation
from src.reseau.types.GuildRankPublicInformation import GuildRankPublicInformation
from src.reseau.types.HavenBagFurnitureInformation import HavenBagFurnitureInformation
from src.reseau.types.ApplicationPlayerInformation import ApplicationPlayerInformation
from src.reseau.types.GuildApplicationInformation import GuildApplicationInformation
from src.reseau.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from src.reseau.types.GuildLogbookChestActivity import GuildLogbookChestActivity
from src.reseau.types.GuildLevelUpActivity import GuildLevelUpActivity
from src.reseau.types.GuildPaddockActivity import GuildPaddockActivity
from src.reseau.types.GuildPlayerFlowActivity import GuildPlayerFlowActivity
from src.reseau.types.GuildPlayerRankUpdateActivity import GuildPlayerRankUpdateActivity
from src.reseau.types.GuildRankActivity import GuildRankActivity
from src.reseau.types.GuildUnlockNewTabActivity import GuildUnlockNewTabActivity
from src.reseau.types.GuildRecruitmentInformation import GuildRecruitmentInformation
from src.reseau.types.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
from src.reseau.types.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from src.reseau.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from src.reseau.types.TaxCollectorFightersInformation import TaxCollectorFightersInformation
from src.reseau.types.TaxCollectorGuildInformations import TaxCollectorGuildInformations
from src.reseau.types.TaxCollectorInformations import TaxCollectorInformations
from src.reseau.types.TaxCollectorLootInformations import TaxCollectorLootInformations
from src.reseau.types.TaxCollectorMovement import TaxCollectorMovement
from src.reseau.types.TaxCollectorWaitingForHelpInformations import TaxCollectorWaitingForHelpInformations
from src.reseau.types.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
from src.reseau.types.AccountHouseInformations import AccountHouseInformations
from src.reseau.types.HouseGuildedInformations import HouseGuildedInformations
from src.reseau.types.HouseInformations import HouseInformations
from src.reseau.types.HouseInformationsForGuild import HouseInformationsForGuild
from src.reseau.types.HouseInformationsForSell import HouseInformationsForSell
from src.reseau.types.HouseInformationsInside import HouseInformationsInside
from src.reseau.types.HouseInstanceInformations import HouseInstanceInformations
from src.reseau.types.HouseOnMapInformations import HouseOnMapInformations
from src.reseau.types.Idol import Idol
from src.reseau.types.PartyIdol import PartyIdol
from src.reseau.types.InteractiveElement import InteractiveElement
from src.reseau.types.InteractiveElementNamedSkill import InteractiveElementNamedSkill
from src.reseau.types.InteractiveElementSkill import InteractiveElementSkill
from src.reseau.types.InteractiveElementWithAgeBonus import InteractiveElementWithAgeBonus
from src.reseau.types.MapObstacle import MapObstacle
from src.reseau.types.StatedElement import StatedElement
from src.reseau.types.SkillActionDescription import SkillActionDescription
from src.reseau.types.SkillActionDescriptionCollect import SkillActionDescriptionCollect
from src.reseau.types.SkillActionDescriptionCraft import SkillActionDescriptionCraft
from src.reseau.types.SkillActionDescriptionTimed import SkillActionDescriptionTimed
from src.reseau.types.TeleportDestination import TeleportDestination
from src.reseau.types.StorageTabInformation import StorageTabInformation
from src.reseau.types.UpdatedStorageTabInformation import UpdatedStorageTabInformation
from src.reseau.types.RecycledItem import RecycledItem
from src.reseau.types.EntityLook import EntityLook
from src.reseau.types.IndexedEntityLook import IndexedEntityLook
from src.reseau.types.SubEntity import SubEntity
from src.reseau.types.ItemDurability import ItemDurability
from src.reseau.types.MountClientData import MountClientData
from src.reseau.types.UpdateMountBooleanCharacteristic import UpdateMountBooleanCharacteristic
from src.reseau.types.UpdateMountCharacteristic import UpdateMountCharacteristic
from src.reseau.types.UpdateMountIntegerCharacteristic import UpdateMountIntegerCharacteristic
from src.reseau.types.MountInformationsForPaddock import MountInformationsForPaddock
from src.reseau.types.PaddockBuyableInformations import PaddockBuyableInformations
from src.reseau.types.PaddockContentInformations import PaddockContentInformations
from src.reseau.types.PaddockGuildedInformations import PaddockGuildedInformations
from src.reseau.types.PaddockInformations import PaddockInformations
from src.reseau.types.PaddockInformationsForSell import PaddockInformationsForSell
from src.reseau.types.PaddockInstancesInformations import PaddockInstancesInformations
from src.reseau.types.PaddockItem import PaddockItem
from src.reseau.types.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
from src.reseau.types.EntitiesPreset import EntitiesPreset
from src.reseau.types.ForgettableSpellsPreset import ForgettableSpellsPreset
from src.reseau.types.FullStatsPreset import FullStatsPreset
from src.reseau.types.IconNamedPreset import IconNamedPreset
from src.reseau.types.IdolsPreset import IdolsPreset
from src.reseau.types.ItemForPreset import ItemForPreset
from src.reseau.types.ItemsPreset import ItemsPreset
from src.reseau.types.Preset import Preset
from src.reseau.types.PresetsContainerPreset import PresetsContainerPreset
from src.reseau.types.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
from src.reseau.types.SpellForPreset import SpellForPreset
from src.reseau.types.SpellsPreset import SpellsPreset
from src.reseau.types.StatsPreset import StatsPreset
from src.reseau.types.AllianceInsiderPrismInformation import AllianceInsiderPrismInformation
from src.reseau.types.AlliancePrismInformation import AlliancePrismInformation
from src.reseau.types.PrismFightersInformation import PrismFightersInformation
from src.reseau.types.PrismGeolocalizedInformation import PrismGeolocalizedInformation
from src.reseau.types.PrismInformation import PrismInformation
from src.reseau.types.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from src.reseau.types.Shortcut import Shortcut
from src.reseau.types.ShortcutEmote import ShortcutEmote
from src.reseau.types.ShortcutEntitiesPreset import ShortcutEntitiesPreset
from src.reseau.types.ShortcutObject import ShortcutObject
from src.reseau.types.ShortcutObjectIdolsPreset import ShortcutObjectIdolsPreset
from src.reseau.types.ShortcutObjectItem import ShortcutObjectItem
from src.reseau.types.ShortcutObjectPreset import ShortcutObjectPreset
from src.reseau.types.ShortcutSmiley import ShortcutSmiley
from src.reseau.types.ShortcutSpell import ShortcutSpell
from src.reseau.types.AbstractSocialGroupInfos import AbstractSocialGroupInfos
from src.reseau.types.AlliancedGuildFactSheetInformations import AlliancedGuildFactSheetInformations
from src.reseau.types.AllianceFactSheetInformations import AllianceFactSheetInformations
from src.reseau.types.GuildFactSheetInformations import GuildFactSheetInformations
from src.reseau.types.GuildInAllianceVersatileInformations import GuildInAllianceVersatileInformations
from src.reseau.types.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
from src.reseau.types.GuildVersatileInformations import GuildVersatileInformations
from src.reseau.types.StartupActionAddObject import StartupActionAddObject
from src.reseau.types.TrustCertificate import TrustCertificate
from src.reseau.types.Version import Version
from src.reseau.types.BufferInformation import BufferInformation
class TypesFactory:
    id_class = {
    "3354": AbstractPlayerSearchInformation,
    "7861": AccountTagInformation,
    "3129": PlayerSearchCharacterNameInformation,
    "5463": PlayerSearchTagInformation,
    "3816": StatisticData,
    "8667": StatisticDataBoolean,
    "1264": StatisticDataByte,
    "6188": StatisticDataInt,
    "9644": StatisticDataShort,
    "9721": StatisticDataString,
    "7562": GameServerInformations,
    "8543": Achievement,
    "4559": AchievementAchieved,
    "6135": AchievementAchievedRewardable,
    "9536": AchievementObjective,
    "1120": AchievementStartedObjective,
    "9699": FightDispellableEffectExtendedInformations,
    "4443": AbstractFightDispellableEffect,
    "455": FightTemporaryBoostEffect,
    "9112": FightTemporaryBoostStateEffect,
    "5975": FightTemporaryBoostWeaponDamagesEffect,
    "2": FightTemporarySpellBoostEffect,
    "6345": FightTemporarySpellImmunityEffect,
    "8023": FightTriggeredEffect,
    "4268": GameActionMark,
    "8580": GameActionMarkedCell,
    "1030": ServerSessionConstant,
    "9087": ServerSessionConstantInteger,
    "1241": ServerSessionConstantLong,
    "89": ServerSessionConstantString,
    "4983": AbstractCharacterInformation,
    "840": CharacterBasicMinimalInformations,
    "7909": CharacterMinimalAllianceInformations,
    "1492": CharacterMinimalGuildInformations,
    "6496": CharacterMinimalGuildPublicInformations,
    "8205": CharacterMinimalInformations,
    "3999": CharacterMinimalPlusLookAndGradeInformations,
    "293": CharacterMinimalPlusLookInformations,
    "6870": ActorAlignmentInformations,
    "7926": ActorExtendedAlignmentInformations,
    "6503": AlterationInfo,
    "9991": CharacterCharacteristic,
    "9854": CharacterCharacteristicDetailed,
    "2462": CharacterCharacteristics,
    "7582": CharacterCharacteristicsInformations,
    "3823": CharacterCharacteristicValue,
    "8178": CharacterSpellModification,
    "6677": CharacterUsableCharacteristicDetailed,
    "8446": CharacterBaseInformations,
    "9829": CharacterHardcoreOrEpicInformations,
    "234": CharacterRemodelingInformation,
    "2055": CharacterToRemodelInformations,
    "4836": RemodelingInformation,
    "4146": DebtInformation,
    "9864": KamaDebtInformation,
    "1005": PlayerNote,
    "3391": ActorRestrictionsInformations,
    "7922": PlayerStatus,
    "9255": PlayerStatusExtended,
    "2130": ActorOrientation,
    "8641": EntityDispositionInformations,
    "7424": EntityMovementInformations,
    "1235": FightEntityDispositionInformations,
    "5501": GameContextActorInformations,
    "2634": GameContextActorPositionInformations,
    "5325": GameRolePlayTaxCollectorInformations,
    "1201": IdentifiedEntityDispositionInformations,
    "3674": MapCoordinates,
    "1411": MapCoordinatesAndId,
    "1105": MapCoordinatesExtended,
    "1156": TaxCollectorStaticExtendedInformations,
    "205": TaxCollectorStaticInformations,
    "4687": AbstractFightTeamInformations,
    "6596": BaseSpawnMonsterInformation,
    "2780": FightAllianceTeamInformations,
    "3080": FightCommonInformations,
    "5194": FightExternalInformations,
    "9": FightLoot,
    "8149": FightLootObject,
    "2083": FightOptionsInformations,
    "7905": FightResultAdditionalData,
    "2849": FightResultExperienceData,
    "3263": FightResultFighterListEntry,
    "3443": FightResultListEntry,
    "4801": FightResultMutantListEntry,
    "8644": FightResultPlayerListEntry,
    "398": FightResultPvpData,
    "2626": FightResultTaxCollectorListEntry,
    "7840": FightStartingPositions,
    "9065": FightTeamInformations,
    "1837": FightTeamLightInformations,
    "3689": FightTeamMemberCharacterInformations,
    "6520": FightTeamMemberEntityInformation,
    "697": FightTeamMemberInformations,
    "3828": FightTeamMemberMonsterInformations,
    "4581": FightTeamMemberTaxCollectorInformations,
    "2672": FightTeamMemberWithAllianceCharacterInformations,
    "6559": GameContextBasicSpawnInformation,
    "3563": GameContextSummonsInformation,
    "2861": GameFightAIInformations,
    "9900": GameFightCharacterInformations,
    "5027": GameFightCharacteristics,
    "470": GameFightEffectTriggerCount,
    "1134": GameFightEntityInformation,
    "6483": GameFightFighterEntityLightInformation,
    "690": GameFightFighterInformations,
    "7931": GameFightFighterLightInformations,
    "8085": GameFightFighterMonsterLightInformations,
    "2767": GameFightFighterNamedInformations,
    "7177": GameFightFighterNamedLightInformations,
    "4561": GameFightFighterTaxCollectorLightInformations,
    "9487": GameFightMonsterInformations,
    "3027": GameFightMonsterWithAlignmentInformations,
    "7944": GameFightMutantInformations,
    "3021": GameFightResumeSlaveInfo,
    "4199": GameFightSpellCooldown,
    "167": GameFightTaxCollectorInformations,
    "7811": SpawnCharacterInformation,
    "9037": SpawnCompanionInformation,
    "405": SpawnInformation,
    "2523": SpawnMonsterInformation,
    "3791": SpawnScaledMonsterInformation,
    "2649": AllianceInformations,
    "8950": AlternativeMonstersInGroupLightInformations,
    "1613": AnomalySubareaInformation,
    "1845": AtlasPointsInformations,
    "4259": BasicAllianceInformations,
    "489": BasicGuildInformations,
    "5227": BasicNamedAllianceInformations,
    "1906": GameRolePlayActorInformations,
    "4799": GameRolePlayCharacterInformations,
    "5866": GameRolePlayGroupMonsterInformations,
    "2209": GameRolePlayGroupMonsterWaveInformations,
    "1299": GameRolePlayHumanoidInformations,
    "3527": GameRolePlayMerchantInformations,
    "9718": GameRolePlayMountInformations,
    "9752": GameRolePlayMutantInformations,
    "419": GameRolePlayNamedActorInformations,
    "1050": GameRolePlayNpcInformations,
    "5987": GameRolePlayNpcWithQuestInformations,
    "7346": GameRolePlayPortalInformations,
    "743": GameRolePlayPrismInformations,
    "1810": GameRolePlayTreasureHintInformations,
    "5133": GroupMonsterStaticInformations,
    "5525": GroupMonsterStaticInformationsWithAlternatives,
    "7649": GuildInAllianceInformations,
    "2826": GuildInformations,
    "6597": HumanInformations,
    "1697": HumanOption,
    "255": HumanOptionAlliance,
    "7900": HumanOptionEmote,
    "44": HumanOptionFollowers,
    "6489": HumanOptionGuild,
    "6890": HumanOptionObjectUse,
    "6238": HumanOptionOrnament,
    "5177": HumanOptionSkillUse,
    "7073": HumanOptionSpeedMultiplier,
    "157": HumanOptionTitle,
    "9972": MonsterBoosts,
    "3301": MonsterInGroupInformations,
    "8269": MonsterInGroupLightInformations,
    "2912": ObjectItemInRolePlay,
    "1555": AlignmentWarEffortInformation,
    "4729": BreachBranch,
    "8289": BreachReward,
    "4455": ExtendedBreachBranch,
    "5736": ExtendedLockedBreachBranch,
    "925": ArenaLeagueRanking,
    "3258": ArenaRankInfos,
    "413": ArenaRanking,
    "1569": LeagueFriendInformations,
    "1740": DecraftedItemStackInfo,
    "5624": JobBookSubscription,
    "1811": JobCrafterDirectoryEntryJobInfo,
    "336": JobCrafterDirectoryEntryPlayerInfo,
    "10": JobCrafterDirectoryListEntry,
    "5830": JobCrafterDirectorySettings,
    "6378": JobDescription,
    "8463": JobExperience,
    "7349": MapNpcQuestInfo,
    "2868": DungeonPartyFinderPlayer,
    "7186": NamedPartyTeam,
    "4963": NamedPartyTeamWithOutcome,
    "5192": PartyGuestInformations,
    "7053": PartyInvitationMemberInformations,
    "1403": PartyMemberArenaInformations,
    "3797": PartyMemberGeoPosition,
    "7293": PartyMemberInformations,
    "3337": PartyEntityBaseInformation,
    "1645": PartyEntityMemberInformation,
    "4439": GameRolePlayNpcQuestFlag,
    "1716": QuestActiveDetailedInformations,
    "2561": QuestActiveInformations,
    "1202": QuestObjectiveInformations,
    "7979": QuestObjectiveInformationsWithCompletion,
    "8401": PortalInformation,
    "4912": TreasureHuntFlag,
    "5044": TreasureHuntStep,
    "277": TreasureHuntStepDig,
    "3878": TreasureHuntStepFight,
    "9440": TreasureHuntStepFollowDirection,
    "8970": TreasureHuntStepFollowDirectionToHint,
    "2724": TreasureHuntStepFollowDirectionToPOI,
    "3737": BidExchangerObjectInfo,
    "7038": ForgettableSpellItem,
    "8060": GoldItem,
    "6716": Item,
    "1090": ObjectEffects,
    "1144": ObjectItem,
    "2712": ObjectItemGenericQuantity,
    "1764": ObjectItemInformationWithQuantity,
    "886": ObjectItemMinimalInformation,
    "7100": ObjectItemNotInContainer,
    "5575": ObjectItemQuantity,
    "1032": ObjectItemQuantityPriceDateEffects,
    "7439": ObjectItemToSell,
    "3734": ObjectItemToSellInBid,
    "4115": ObjectItemToSellInHumanVendorShop,
    "8056": ObjectItemToSellInNpcShop,
    "6968": SellerBuyerDescriptor,
    "5286": SpellItem,
    "9999": ObjectEffect,
    "8986": ObjectEffectCreature,
    "8113": ObjectEffectDate,
    "2887": ObjectEffectDice,
    "5388": ObjectEffectDuration,
    "5031": ObjectEffectInteger,
    "502": ObjectEffectLadder,
    "4732": ObjectEffectMinMax,
    "3395": ObjectEffectMount,
    "2555": ObjectEffectString,
    "5440": EntityInformation,
    "7715": ProtectedEntityWaitingForHelpInfo,
    "8614": FinishMoveInformations,
    "8340": AbstractContactInformations,
    "7350": AcquaintanceInformation,
    "2998": AcquaintanceOnlineInformation,
    "2931": FriendInformations,
    "6579": FriendOnlineInformations,
    "522": FriendSpouseInformations,
    "8681": FriendSpouseOnlineInformations,
    "3826": IgnoredInformations,
    "4298": IgnoredOnlineInformations,
    "7288": Contribution,
    "9960": GuildEmblem,
    "3151": GuildMember,
    "5401": GuildRankInformation,
    "70": GuildRankMinimalInformation,
    "2314": GuildRankPublicInformation,
    "5802": HavenBagFurnitureInformation,
    "5249": ApplicationPlayerInformation,
    "976": GuildApplicationInformation,
    "324": GuildLogbookEntryBasicInformation,
    "1251": GuildLogbookChestActivity,
    "9284": GuildLevelUpActivity,
    "3725": GuildPaddockActivity,
    "5181": GuildPlayerFlowActivity,
    "5102": GuildPlayerRankUpdateActivity,
    "9683": GuildRankActivity,
    "8199": GuildUnlockNewTabActivity,
    "7615": GuildRecruitmentInformation,
    "403": AdditionalTaxCollectorInformations,
    "2378": TaxCollectorBasicInformations,
    "7396": TaxCollectorComplementaryInformations,
    "9488": TaxCollectorFightersInformation,
    "146": TaxCollectorGuildInformations,
    "7255": TaxCollectorInformations,
    "8279": TaxCollectorLootInformations,
    "7087": TaxCollectorMovement,
    "4172": TaxCollectorWaitingForHelpInformations,
    "7015": HavenBagRoomPreviewInformation,
    "4256": AccountHouseInformations,
    "6289": HouseGuildedInformations,
    "1082": HouseInformations,
    "5756": HouseInformationsForGuild,
    "3668": HouseInformationsForSell,
    "5175": HouseInformationsInside,
    "3926": HouseInstanceInformations,
    "7781": HouseOnMapInformations,
    "7456": Idol,
    "466": PartyIdol,
    "3496": InteractiveElement,
    "6640": InteractiveElementNamedSkill,
    "1464": InteractiveElementSkill,
    "3253": InteractiveElementWithAgeBonus,
    "5431": MapObstacle,
    "5825": StatedElement,
    "4309": SkillActionDescription,
    "1601": SkillActionDescriptionCollect,
    "9626": SkillActionDescriptionCraft,
    "7041": SkillActionDescriptionTimed,
    "2810": TeleportDestination,
    "5653": StorageTabInformation,
    "5533": UpdatedStorageTabInformation,
    "729": RecycledItem,
    "3447": EntityLook,
    "3771": IndexedEntityLook,
    "8816": SubEntity,
    "4082": ItemDurability,
    "9503": MountClientData,
    "32": UpdateMountBooleanCharacteristic,
    "4350": UpdateMountCharacteristic,
    "4473": UpdateMountIntegerCharacteristic,
    "967": MountInformationsForPaddock,
    "706": PaddockBuyableInformations,
    "8604": PaddockContentInformations,
    "8850": PaddockGuildedInformations,
    "7920": PaddockInformations,
    "6240": PaddockInformationsForSell,
    "6147": PaddockInstancesInformations,
    "1800": PaddockItem,
    "95": CharacterCharacteristicForPreset,
    "7295": EntitiesPreset,
    "2769": ForgettableSpellsPreset,
    "5449": FullStatsPreset,
    "1753": IconNamedPreset,
    "2551": IdolsPreset,
    "2797": ItemForPreset,
    "5024": ItemsPreset,
    "5250": Preset,
    "2486": PresetsContainerPreset,
    "1928": SimpleCharacterCharacteristicForPreset,
    "7670": SpellForPreset,
    "882": SpellsPreset,
    "5265": StatsPreset,
    "471": AllianceInsiderPrismInformation,
    "622": AlliancePrismInformation,
    "5465": PrismFightersInformation,
    "1260": PrismGeolocalizedInformation,
    "4160": PrismInformation,
    "7729": PrismSubareaEmptyInfo,
    "9291": Shortcut,
    "7402": ShortcutEmote,
    "3212": ShortcutEntitiesPreset,
    "8391": ShortcutObject,
    "4281": ShortcutObjectIdolsPreset,
    "7189": ShortcutObjectItem,
    "5702": ShortcutObjectPreset,
    "8039": ShortcutSmiley,
    "8014": ShortcutSpell,
    "4610": AbstractSocialGroupInfos,
    "1860": AlliancedGuildFactSheetInformations,
    "5647": AllianceFactSheetInformations,
    "570": GuildFactSheetInformations,
    "200": GuildInAllianceVersatileInformations,
    "766": GuildInsiderFactSheetInformations,
    "9976": GuildVersatileInformations,
    "3679": StartupActionAddObject,
    "6622": TrustCertificate,
    "7693": Version,
    "5420": BufferInformation
    }
    
    @classmethod
    def get_instance_id(cls,id,content):
        return cls.id_class[str(id)](content)
    